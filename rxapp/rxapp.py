"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""


def ind3ex() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text("Get started by editing ", rx.code(filename)),
            rx.button(
                "Check out our docs!",
                on_click=lambda: rx.redirect(docs_url),
                size="4",
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


def index2():
    return rx.hstack(
        rx.heading("Welcome to Sam's place!", size="9", align="left"),
        rx.heading(
            "My projects",
            on_click=lambda: rx.redirect("#projects"),
            size="9",
            align="center",
        ),
        spacing="7",
        font_size="2em",
    )


def index3():
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.spacer(),
                rx.heading("AI personal landing page", font_size="1.5em"),
                rx.spacer(),
                rx.color_mode.icon(),
                rx.color_mode.switch(),
                width="100%",
            ),
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "Welcome to Reflex! Providing insights about Reflex, think about innovating in python. Here are some quick links:",
                        size="9",
                    ),
                    rx.unordered_list(
                        rx.list_item(
                            rx.text("Website: ", weight="bold"),
                            rx.link(
                                "🔗 Reflex Site",
                                href="https:reflex.dev",
                            ),
                        ),
                        rx.list_item(
                            rx.text("Twitter: ", weight="bold"),
                            rx.link(
                                "🔗 @getreflex",
                                href="https://twitter.com/getreflex",
                            ),
                        ),
                        rx.list_item(
                            rx.text("Github: ", weight="bold"),
                            rx.link(
                                "🔗 reflex-dev / reflex",
                                href="https://github.com/reflex-dev/reflex",
                            ),
                        ),
                        spacing="2",
                    ),
                    rx.text(
                        "Discover the power of Reflex with these commands:",
                    ),
                    rx.unordered_list(
                        rx.list_item(
                            rx.code("/tell me about Reflex"),
                        ),
                        rx.list_item(
                            rx.code("/how do I install Reflex"),
                        ),
                        spacing="2",
                    ),
                    rx.text(
                        "Ask a personal AI assistant a question about Reflex or explore some of the projects below:"
                    ),
                    rx.unordered_list(
                        rx.list_item(
                            rx.link(
                                "🔗 Reflex Site",
                                href="https:reflex.dev",
                            ),
                        ),
                        rx.list_item(
                            rx.link(
                                "🔗 @getreflex",
                                href="https://twitter.com/getreflex",
                            ),
                        ),
                        rx.list_item(
                            rx.link(
                                "🔗 reflex-dev / reflex",
                                href="https://github.com/reflex-dev/reflex",
                            ),
                        ),
                        spacing="2",
                    ),
                    width="65%",
                ),
                rx.container(
                    rx.color_mode_cond(
                        rx.image(src="/logos/light/reflex.svg", height="4em"),
                        rx.image(src="/logos/dark/reflex.svg", height="4em"),
                    ),
                    width="35%",
                ),
                spacing="7",
            ),
            width="70em",
            background_color=rx.color("mauve", 1),
            padding="2em",
            align="center",
            border_radius="1em",
            margin_top="52px",
            margin_bottom="24px",
            margin="52px",
        ),
        width="100%",
        height="100vh",
        background="#EEE9DA",
    )


def navbar():
    return rx.hstack(
        rx.hstack(
            rx.image(src="/favicon.ico", width="2em"),
            rx.heading("Sammy sandbox", font_size="2em"),
        ),
        rx.divider(orientation="vertical", size="4"),
        rx.box(
            rx.flex(
                rx.link(
                    rx.text(
                        "Projects",
                        color=rx.color("mauve", 11),
                        font_size="1em",
                    ),
                    href="#projects",
                ),
                rx.divider(orientation="vertical", size="4"),
                rx.link(
                    rx.text("Stats", color=rx.color("amber"), font_size="1em"),
                    href="#stats",
                ),
                spacing="5",
            ),
        ),
        rx.spacer(),
        rx.menu.root(rx.menu.trigger(rx.button("Menu"))),
        position="fixed",
        top="0px",
        padding="1em",
        height="4em",
        width="100%",
        z_index="5",
    )


def content():
    return rx.box(
        rx.heading("Welcome to My App"), rx.text("This is the main content")
    )


def index():
    return rx.box(
        navbar(),
        rx.center(
            content(),
            padding_top="16em",
            max_width="560em",
            width="100%",
            margin_y="2em",
            padding="2em",
        ),
    )


app = rx.App()
app.add_page(index)
