import flet as ft
from flet_share_plus import SharePlus


def main(page: ft.Page):
    page.title = "SharePlus Demo"
    page.padding = 20

    # Text fields for content to share
    text_to_share = ft.TextField(
        label="Text to share",
        multiline=True,
        min_lines=2,
        value="Text to share: https://flet.dev",
        width=400,
    )

    subject_to_share = ft.TextField(
        label="Subject (optional)",
        value="Email subject",
        width=400,
    )

    # File path input
    file_path = ft.TextField(
        label="File path to share (optional)",
        width=400,
    )

    # Status text to show share results
    status_text = ft.Text(size=16)

    # Create share service control (non-visual)
    share = SharePlus(
        on_share_completed=lambda e: status_text.update(
            value=f"Sharing completed with: {e.data}"
        ),
        on_share_dismissed=lambda e: status_text.update(value="Sharing cancelled"),
    )

    # Handler functions for share buttons
    def share_text(e):
        share.share_text(
            text=text_to_share.value,
            subject=subject_to_share.value,
        )

    def share_file(e):
        if file_path.value:
            share.share_files(
                file_paths=[file_path.value],
                text=text_to_share.value,
            )
        else:
            status_text.value = "Enter a valid file path"
            status_text.update()

    # Add controls to the page
    page.add(
        ft.Column(
            [
                ft.Text("SharePlus Demo", size=24, weight=ft.FontWeight.BOLD),
                text_to_share,
                subject_to_share,
                file_path,
                ft.Row(
                    [
                        ft.ElevatedButton("Share Text", on_click=share_text),
                        ft.ElevatedButton("Share File", on_click=share_file),
                        ft.IconButton(
                            icon=ft.Icons.SHARE,
                            tooltip="Share",
                            on_click=share_text,
                        ),
                    ],
                    spacing=10,
                ),
                status_text,
            ],
            spacing=20,
        ),
        share,  # Add the non-visual share service
    )


ft.app(main)
