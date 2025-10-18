import reflex as rx
from typing import TypedDict


class Feature(TypedDict):
    icon: str
    title: str
    description: str


class Stat(TypedDict):
    value: str
    label: str


class State(rx.State):
    """The base state for the app."""

    current_section: str = "home"
    performance_features: list[Feature] = [
        {
            "icon": "zap",
            "title": "Optimized Hashrate",
            "description": "Our custom algorithms are fine-tuned for NVIDIA and AMD GPUs, delivering maximum hashrate.",
        },
        {
            "icon": "activity",
            "title": "Real-Time Analytics",
            "description": "Monitor every aspect of your mining operation in real-time with our detailed analytics dashboard.",
        },
        {
            "icon": "shield",
            "title": "Stable & Secure",
            "description": "Built with stability in mind, LAPIS ensures your rigs are mining 24/7 without interruptions.",
        },
    ]
    pool_features: list[Feature] = [
        {
            "icon": "briefcase",
            "title": "Pool Templates",
            "description": "One-click connect to major mining pools with our pre-configured templates.",
        },
        {
            "icon": "shuffle",
            "title": "Failover Pools",
            "description": "Automatically switch to a backup pool in case of a connection failure, ensuring zero downtime.",
        },
        {
            "icon": "settings-2",
            "title": "Custom Configuration",
            "description": "Advanced users can fine-tune every parameter for custom or private pool connections.",
        },
    ]
    dashboard_features: list[Feature] = [
        {
            "icon": "layout-dashboard",
            "title": "Unified Control",
            "description": "Manage all your rigs, wallets, and configurations from a single, intuitive interface.",
        },
        {
            "icon": "smartphone",
            "title": "Mobile Friendly",
            "description": "Access your dashboard from anywhere, on any device, with our fully responsive design.",
        },
        {
            "icon": "bell",
            "title": "Custom Alerts",
            "description": "Set up custom notifications for hashrate drops, temperature warnings, and more.",
        },
    ]
    support_features: list[Feature] = [
        {
            "icon": "message-square",
            "title": "Community Discord",
            "description": "Join our active Discord community to get help from fellow miners and our support staff.",
        },
        {
            "icon": "book-open",
            "title": "Extensive Docs",
            "description": "Our comprehensive documentation covers everything from basic setup to advanced tweaking.",
        },
        {
            "icon": "mail",
            "title": "Email Support",
            "description": "Get direct, private support from our dedicated team for any complex issues you encounter.",
        },
    ]
    stats: list[Stat] = [
        {"value": "1.2 EH/s", "label": "Network Hashrate"},
        {"value": "99.9%", "label": "Uptime Guarantee"},
        {"value": "50k+", "label": "Active Miners"},
        {"value": "<5ms", "label": "Pool Latency"},
    ]

    @rx.event
    def set_section(self, section_id: str):
        self.current_section = section_id