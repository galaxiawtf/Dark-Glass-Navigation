import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.p("© 2024 LAPIS Inc. All rights reserved."),
                class_name="text-sm text-gray-400",
            ),
            rx.el.div(
                rx.el.a(rx.icon("twitter", class_name="h-5 w-5"), href="#"),
                rx.el.a(rx.icon("github", class_name="h-5 w-5"), href="#"),
                rx.el.a(rx.icon("message-square", class_name="h-5 w-5"), href="#"),
                class_name="flex items-center space-x-4 text-gray-400",
            ),
            class_name="container mx-auto px-4 py-6 flex justify-between items-center",
        ),
        class_name="bg-gray-900 border-t border-white/10",
    )