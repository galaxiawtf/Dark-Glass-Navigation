import reflex as rx
from app.states.state import State


def nav_item(text: str, section_id: str, icon_name: str) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(
                icon_name,
                class_name="h-5 w-5 md:h-6 md:w-6 transition-all duration-300",
            ),
            rx.el.span(
                text,
                class_name="absolute left-1/2 -translate-x-1/2 top-14 md:top-16 opacity-0 group-hover:opacity-100 group-hover:top-12 md:group-hover:top-14 transition-all duration-300 text-xs font-medium bg-gray-800 text-white px-2 py-1 rounded-md",
            ),
            class_name="relative flex items-center justify-center h-10 w-10 md:h-12 md:w-12 rounded-full transition-all duration-300 cursor-pointer group",
        ),
        href=f"#{section_id}",
        class_name=rx.cond(
            State.current_section == section_id,
            "bg-blue-500/30 text-blue-300 rounded-full p-1",
            "text-gray-400 hover:text-white hover:bg-white/10 rounded-full p-1 transition-all duration-300",
        ),
        on_click=lambda: State.set_section(section_id),
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            nav_item("Home", "home", "home"),
            nav_item("Performance", "performance", "bar-chart-2"),
            nav_item("Pools", "pools", "server"),
            nav_item("Dashboard", "dashboard", "layout-grid"),
            nav_item("Support", "support", "life-buoy"),
            class_name="flex items-center justify-center space-x-2 md:space-x-4",
        ),
        class_name="fixed bottom-6 left-1/2 -translate-x-1/2 z-50 bg-gray-900/70 backdrop-blur-lg border border-white/10 rounded-full py-2 px-4 md:py-3 md:px-6 shadow-2xl",
    )