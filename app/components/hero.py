import reflex as rx


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                class_name="absolute inset-0 bg-grid-white/5 [mask-image:linear-gradient(to_bottom,white_10%,transparent_90%)]"
            ),
            rx.el.h1(
                "Unleash Mining Power with",
                rx.el.span(
                    " LAPIS",
                    class_name="text-transparent bg-clip-text bg-gradient-to-br from-blue-400 via-teal-400 to-green-400",
                ),
                class_name="text-4xl md:text-6xl lg:text-7xl font-extrabold text-white tracking-tighter text-center leading-tight",
            ),
            rx.el.p(
                "The next-generation crypto mining software, engineered for peak performance and simplicity.",
                class_name="mt-6 text-lg md:text-xl text-gray-300 max-w-2xl text-center",
            ),
            rx.el.div(
                rx.el.button(
                    "Download for Free",
                    rx.icon("arrow-down-to-line", class_name="ml-2"),
                    class_name="flex items-center bg-gradient-to-r from-blue-500 to-teal-500 text-white px-8 py-3 rounded-full font-semibold text-lg hover:shadow-lg hover:shadow-teal-500/30 transform transition-all duration-300",
                ),
                rx.el.button(
                    "View Docs",
                    rx.icon("book-open", class_name="ml-2"),
                    class_name="flex items-center bg-gray-800/80 text-white px-8 py-3 rounded-full font-semibold border border-white/20 hover:bg-gray-700/80 transition-all duration-300",
                ),
                class_name="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4",
            ),
            class_name="relative flex flex-col items-center justify-center min-h-[90vh] px-4 py-16 text-center",
        ),
        id="home",
        class_name="w-full",
    )