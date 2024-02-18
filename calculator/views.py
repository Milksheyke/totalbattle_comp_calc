from django.shortcuts import render
from django.http import HttpResponse

from .conversion_equations import (
    calculate_total_silver,
    calculate_category_total,
    calculate_guards_total_cost,
    calculate_merc_cost,
    calculate_monster_cost,
    resources,
    guardsmen,
    mercs,
    monsters,
    engineers,
    specialists,
    categories,
)


def human_readable_number(value):
    for unit in ["", "k", "M", "B", "T"]:
        if abs(value) < 1000:
            return f"{value:3.2f}{unit}"
        value /= 1000
    return f"{value:3.2f}T"


def calculate_compensation(request):
    if request.method == "POST":
        # Initialize a dictionary to hold casualties data
        casualties_data = {}

        # Iterate over each category and its units
        for category, units in categories.items():
            category_casualties = {}
            for unit in units:
                # Construct the form field name
                field_name = f"{category}_{unit}"
                # Extract the number of casualties from the POST data
                casualties = request.POST.get(field_name, 0)
                try:
                    casualties = int(casualties)
                except ValueError:
                    casualties = 0  # Default to 0 if conversion fails

                if casualties > 0:  # Only add units with casualties
                    category_casualties[unit] = casualties

            if category_casualties:
                casualties_data[category] = category_casualties

        total_silver = calculate_total_silver(**casualties_data)
        readable_total = human_readable_number(total_silver)

        return render(request, "calc_results.html", {"readable_total": readable_total})
    else:
        return render(request, "calc_form.html", {"categories": categories})
