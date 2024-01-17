#!/usr/bin/python3

import sys
import datadog_api_client
from datadog_api_client.v2 import ApiClient, ApiException
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v2.models import *


def get_dashboard_id(api_key, app_key, dashboard_name):
    # Initialize the Datadog API client
    configuration = datadog_api_client.Configuration()
    configuration.api_key['apiKeyAuth'] = api_key
    configuration.api_key['appKeyAuth'] = app_key

    # Create an instance of the DashboardsApi
    dashboards_api = DashboardsApi(datadog_api_client.ApiClient(configuration))

    try:
        # Get a list of dashboards
        response = dashboards_api.list_dashboards()
        dashboards = response.dashboards

        # Find the dashboard ID by matching the dashboard name
        for dashboard in dashboards:
            if dashboard.title == dashboard_name:
                return dashboard.id

    except ApiException as e:
        print(f"Error: Unable to retrieve the dashboard ID. Code {e.status}, {e.body}")

    return None

def main():

    if len(sys.argv) != 4:
        print(f"Requires: <{sys.argv[0]}> <api_key> <app_key> <dashboard_name>")
        exit(1)

    # Replace these with your actual Datadog API and application keys
    api_key = sys.argv[1]
    app_key = sys.argv[2]

    # Specify the name of the dashboard you want to retrieve the ID for
    dashboard_name = sys.argv[3]

    # Get the dashboard ID
    dashboard_id = get_dashboard_id(api_key, app_key, dashboard_name)

    if dashboard_id is not None:
        print(f"Dashboard ID: {dashboard_id}")
    else:
        print("Dashboard does not exist. Check your arguments again")


if __name__ == "__main__":
    main()
