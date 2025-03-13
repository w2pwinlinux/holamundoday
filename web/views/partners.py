import reflex as rx
import web.styles.styles as styles
from web import constants
from web.components.button import button
from web.components.print_text import print_text
from web.components.terminal_text import terminal_text
from web.components.partner import partner
from web.styles.styles import Size


def partners() -> rx.Component:
    return rx.vstack(
        terminal_text(quoted_text="Patrocinado", end_text=" por"),
        rx.flex(
            partner(
                "/partners/platzi.png",
                "https://platzi.com/BraisconfMX",
                "Estudia programación"
            ),
            partner(
                "/partners/raiola.png",
                "https://mouredev.com/raiola",
                "20% en hosting"
            ),
            partner(
                "/partners/nuwe.png",
                "https://bit.ly/JobOffersNUWE",
                "Aplica a vacantes Tech"
            ),
            partner(
                "/partners/elgato.png",
                "https://elgato.sjv.io/mouredev",
                "5% código ZZ-MOUREDEV"
            ),
            spacing=Size.SMALL.value,
            wrap="wrap"
        ),
        rx.spacer(),
        # rx.text("¿Quieres patrocinar el evento? ¡NO TENGO PALABRAS!"),
        # rx.text(
        #     "Puedes escribirme a ",
        #     rx.link(
        #         "braismoure@mouredev.com",
        #         href="mailto:braismoure@mouredev.com",
        #         is_external=True
        #     ),
        #     " o contactarme a través de mis redes sociales como ",
        #     rx.link(
        #         "@mouredev",
        #         href=constants.MOUREDEV_URL,
        #         is_external=True
        #     ),
        #     "."
        # ),
        # print_text("El patrocinio servirá para pagar los participantes, realizar sorteos y cubrir los gastos de la organización. También se realizarán menciones y aparecerás destacado en todas las comunicaciones relacionadas con el evento."),
        button(
            constants.COFFEE_URL,
            "Colabora con un café",
            "coffee",
            True,
            id="speakers"
        ),
        spacing=Size.DEFAULT.value,
        style=styles.container
    )
