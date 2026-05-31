import gradio as gr

from codeboost.converter import port
from codeboost.runner import compile_and_run, run_python
from codeboost.samples import DEFAULT_PYTHON
from codeboost.styles import CSS


def build_ui() -> gr.Blocks:
    with gr.Blocks(css=CSS, theme=gr.themes.Monochrome(), title="CodeBoost — Python to C++") as ui:
        with gr.Row(equal_height=True):
            with gr.Column(scale=6):
                python = gr.Code(
                    label="Python (original)",
                    value=DEFAULT_PYTHON,
                    language="python",
                    lines=20,
                )
            with gr.Column(scale=6):
                cpp = gr.Code(
                    label="C++ (generated)",
                    value="",
                    language="cpp",
                    lines=20,
                )

        with gr.Row(elem_classes=["controls"]):
            python_run = gr.Button("Run Python", elem_classes=["run-btn", "py"])
            convert = gr.Button("Port to C++", elem_classes=["convert-btn"])
            cpp_run = gr.Button("Run C++", elem_classes=["run-btn", "cpp"])

        with gr.Row(equal_height=True):
            with gr.Column(scale=6):
                python_out = gr.TextArea(label="Python result", lines=8, elem_classes=["py-out"])
            with gr.Column(scale=6):
                cpp_out = gr.TextArea(label="C++ result", lines=8, elem_classes=["cpp-out"])

        convert.click(fn=port, inputs=[python], outputs=[cpp])
        python_run.click(fn=run_python, inputs=[python], outputs=[python_out])
        cpp_run.click(fn=compile_and_run, inputs=[cpp], outputs=[cpp_out])

    return ui


def launch_app(inbrowser: bool = True) -> None:
    build_ui().launch(inbrowser=inbrowser)
