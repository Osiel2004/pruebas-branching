def calcular_costo_adicional(tipo_servicio, cantidad):
    tarifas = {"timbrado_extra": 0.50, "almacenamiento_gb": 5.00}
    costo = tarifas.get(tipo_servicio, 0) * cantidad
    return costo
