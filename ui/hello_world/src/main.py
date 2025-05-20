import flet as ft
import random
import asyncio
import httpx

# ==================== Random Utilities ====================
def get_random_pos():
    return random.randint(-100, 2000)

def get_random_color():
    return random.choice(["blue", "white"])

def get_random_offset():
    return random.randint(1, 5)

def get_random_wait():
    return random.randrange(500, 700, 100)

# ==================== Animated Background ====================
class Thing(ft.Container):
    def __init__(self):
        color = get_random_color()
        super().__init__(
            left=get_random_pos(),
            top=get_random_pos(),
            width=2.5,
            height=2.5,
            shape=ft.BoxShape("circle"),
            bgcolor=color,
            opacity=0,
            offset=ft.Offset(0, 0),
            shadow=ft.BoxShadow(
                spread_radius=20,
                blur_radius=100,
                color=color,
            )
        )
        self.wait = get_random_wait()

    async def animate_thing(self):
        while True:
            self.opacity = 1
            self.offset = ft.Offset(
                get_random_offset() ** 2,
                get_random_offset() ** 2,
            )
            self.update()
            await asyncio.sleep(self.wait / 1000)
            
            self.opacity = 0
            self.offset = ft.Offset(
                get_random_offset() ** 2,
                get_random_offset() ** 2,
            )
            self.update()
            await asyncio.sleep(self.wait / 1000)

# ==================== Fetch Content ====================
async def fetch_content():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://backend:8000/hello_world")
            response.raise_for_status()
            return response.json().get("text", "Default Text")
    except Exception as e:
        print(f"Error fetching content: {e}")
        return "Fallback Content"

# ==================== UI Components ====================
body_style = {
    "width": 700,
    "padding": 15,
    "bgcolor": ft.Colors.with_opacity(0.095, "white"),
    "border_radius": 10,
    "shadow": ft.BoxShadow(
        spread_radius=20,
        blur_radius=45,
        color=ft.Colors.with_opacity(0.45, "black")
    ),
    "alignment": ft.alignment.center
}

class Body(ft.Container):
    def __init__(self, text_content: str):
        super().__init__(**body_style)
        self.content = ft.Column(
            controls=[
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            text_content,
                            ft.TextStyle(
                                size=100,
                                italic=True,
                                font_family="Consolas",
                                weight=ft.FontWeight.W_900,
                                foreground=ft.Paint(
                                    gradient=ft.PaintLinearGradient(
                                        (0, 800), (800, 0),
                                        [ft.Colors.BLUE_900, ft.Colors.PURPLE_400]
                                    )
                                ),
                            ),
                        )
                    ]
                )
            ]
        )

# ==================== Main App ====================
async def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 0

    # Fetch content
    content_text = await fetch_content()
    
    # Create components
    background = ft.Stack(expand=True, controls=[Thing() for _ in range(50)])
    body = Body(content_text)
    
    # Build UI
    page.add(
        ft.Stack(
            expand=True,
            controls=[
                background,
                ft.Column(
                    alignment="center",
                    horizontal_alignment="center",
                    controls=[
                        ft.Row(
                            alignment="center",
                            controls=[body]
                        )
                    ]
                )
            ]
        )
    )

    # Start animations
    await asyncio.gather(*(item.animate_thing() for item in background.controls))

if __name__ == "__main__":
    ft.app(target=main)
