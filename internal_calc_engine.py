# RentalEngine HQ - Core Operational Calculation Array Matrix
def calculate_system_metrics(gross_hauling_revenue, fuel_maintenance_cost, quarry_material_fees):
    total_system_expense = float(fuel_maintenance_cost) + float(quarry_material_fees)
    gross_revenue = float(gross_hauling_revenue)
    true_net_cash_margin = gross_revenue - total_system_expense
    return [gross_revenue, total_system_expense, true_net_cash_margin]
