import reflex as rx
from app.states.state import State, Stat


def stat_item(stat: Stat) -> rx.Component:
    return rx.el.div(
        rx.el.p(stat["value"], class_name="text-4xl font-bold text-white"),
        rx.el.p(stat["label"], class_name="text-sm text-gray-400"),
        class_name="text-center",
    )


def stats_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.foreach(State.stats, stat_item),
                class_name="grid grid-cols-2 md:grid-cols-4 gap-8",
            ),
            class_name="container mx-auto px-4 py-16",
        ),
        class_name="bg-gray-900/50 border-y border-white/10",
    )