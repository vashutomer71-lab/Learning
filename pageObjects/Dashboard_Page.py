from playwright.sync_api import Page, sync_playwright



class FleetDashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.xpath_left_menu_tab = "//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-yb0lig']"
        self.expected_tabs = [
            "Fleet Dashboard",
            "Depots",
            "Chargers",
            "Vehicles",
            "Drivers",
            "Journey",
            "Maintenance",
            "Tickets",
            "Alerts",
            "Customer",
            "Assets",
            "User Management",
            "Pricing"
        ]
        self.xpath_fleets_dashboard_tiles = "//div[@class='text']"

    def verify_left_menu_tabs(self):
        try:
            # Locate all elements matching the XPath
            left_menu_tabs = self.page.locator(self.xpath_left_menu_tab)

            # Wait until at least one element is visible
            left_menu_tabs.first.wait_for(state='visible')

            # Get the count of elements matching the XPath
            count = left_menu_tabs.count()

            # Check if the count matches expected number of tabs
            assert count == len(self.expected_tabs), f"Expected {len(self.expected_tabs)} tabs but found {count}."

            # Iterate through each element and verify its text content
            for i in range(count):
                tab_text = left_menu_tabs.nth(i).text_content().strip()
                expected_text = self.expected_tabs[i]
                assert tab_text == expected_text, f"Tab {i+1} text '{tab_text}' does not match expected '{expected_text}'."

                print(f"Tab {i+1}: {tab_text} - Verified")

            print("All tabs verified successfully.")

        except AssertionError as e:
            # If assertion fails, capture a screenshot
            self.page.screenshot(path="./Screenshots/menu_tab.png")
            raise AssertionError(str(e) + " Screenshot captured.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise

    def verify_fleet_tile(self):
        # Extract the texts of all the tiles
        tiles = self.page.locator(self.xpath_fleets_dashboard_tiles).all_text_contents()

        # Define the expected tiles
        expected_tiles = {"Fleets", "Vehicles", "Depots", "Chargers"}

        # Verify each expected tile is present in the extracted tile names
        missing_tiles = expected_tiles - set(tiles)

        if not missing_tiles:
            print("All expected tiles are present: Fleets, Vehicles, Depots, Chargers")
        else:
            print(f"Missing tiles: {', '.join(missing_tiles)}")
            # Take a screenshot
            self.page.screenshot(path="./Screenshots/fleet_dashboard_tiles.png")
            raise AssertionError(f"Missing tiles: {', '.join(missing_tiles)}")







