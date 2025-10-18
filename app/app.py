import reflex as rx
from app.components.navbar import navbar
from app.components.hero import hero_section
from app.components.content import content_section
from app.components.stats import stats_section
from app.components.footer import footer
from app.states.state import State


def index() -> rx.Component:
    return rx.el.main(
        hero_section(),
        stats_section(),
        content_section(
            "performance",
            "Peak Performance",
            "LAPIS is optimized for maximum hashrate, ensuring you get the most out of your hardware.",
            "from-green-400",
            "to-teal-400",
            State.performance_features,
        ),
        content_section(
            "pools",
            "Mining Pools",
            "Seamlessly connect to top mining pools or configure your own for collaborative mining.",
            "from-blue-400",
            "to-indigo-500",
            State.pool_features,
        ),
        content_section(
            "dashboard",
            "Intuitive Dashboard",
            "Monitor your rigs, track earnings, and manage your operations from a single, clean interface.",
            "from-purple-400",
            "to-pink-500",
            State.dashboard_features,
        ),
        content_section(
            "support",
            "24/7 Support",
            "Our dedicated support team is always available to help you with any issues or questions.",
            "from-yellow-400",
            "to-orange-500",
            State.support_features,
        ),
        footer(),
        navbar(),
        class_name="font-['Inter'] bg-gray-900 bg-gradient-to-br from-gray-900 via-gray-900 to-black text-white selection:bg-purple-500/30",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)