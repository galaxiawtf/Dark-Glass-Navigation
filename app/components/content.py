import reflex as rx
from app.states.state import Feature


def feature_card(feature: Feature) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(feature["icon"], class_name="h-8 w-8 text-blue-400"),
            class_name="p-3 bg-blue-500/10 rounded-full border border-blue-500/20 mb-4 w-fit",
        ),
        rx.el.h3(feature["title"], class_name="text-xl font-semibold text-white mb-2"),
        rx.el.p(feature["description"], class_name="text-gray-400"),
        class_name="bg-gray-800/50 border border-white/10 rounded-xl p-6 h-full flex flex-col justify-start text-left",
    )


def content_section(
    section_id: str,
    title: str,
    description: str,
    color_from: str,
    color_to: str,
    features: list[Feature],
) -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                title,
                class_name=f"text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r {color_from} {color_to}",
            ),
            rx.el.p(description, class_name="mt-4 text-lg text-gray-300 max-w-3xl"),
            rx.el.div(
                rx.foreach(features, feature_card),
                class_name="mt-12 grid grid-cols-1 md:grid-cols-3 gap-8 w-full max-w-6xl",
            ),
            class_name="container mx-auto px-4 py-20 md:py-24 flex flex-col items-center text-center",
        ),
        id=section_id,
        class_name="w-full",
    )