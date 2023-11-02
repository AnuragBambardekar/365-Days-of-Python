import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment

def main(page: Page) -> None:
    page.title = 'My Store'

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        page.views.append(
            View(
                route='/',
                controls=[AppBar(title=Text('Home'), bgcolor='blue'),
                          Text(value='Home', size=30),
                          ElevatedButton(text='Go to Store', on_click=lambda _ : page.go('/store'))
                          ],
                          vertical_alignment=MainAxisAlignment.CENTER,
                          horizontal_alignment=CrossAxisAlignment.CENTER,
                          spacing=26
            )
        )

        # Store
        if page.route == '/store':
            page.views.append(
            View(
                route='/store',
                controls=[AppBar(title=Text('Store'), bgcolor='blue'),
                          Text(value='Store', size=30),
                          ElevatedButton(text='Go Back', on_click=lambda _ : page.go('/'))
                          ],
                          vertical_alignment=MainAxisAlignment.CENTER,
                          horizontal_alignment=CrossAxisAlignment.CENTER,
                          spacing=26
            )
        )
            
        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)
