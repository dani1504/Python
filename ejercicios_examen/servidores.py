SERVIDORES = [
     {
        "id": 101, "nombre": "web-01", "ip": "192.0.2.10", "rol": "web",
        "estado": "encendido", "cpu": 42, "ram": 55,
        "servicios": {"ssh": "activo", "nginx": "activo"},
    },
    {
        "id": 102, "nombre": "web-02", "ip": "192.0.2.11", "rol": "web",
        "estado": "encendido", "cpu": 91, "ram": 82,
        "servicios": {"ssh": "activo", "nginx": "activo"},
    },
    {
        "id": 103, "nombre": "db-01", "ip": "192.0.2.20", "rol": "bd",
        "estado": "encendido", "cpu": 76, "ram": 94,
        "servicios": {"ssh": "activo", "mariadb": "activo"},
    },
    {
        "id": 104, "nombre": "db-02", "ip": "192.0.2.21", "rol": "bd",
        "estado": "apagado", "cpu": 22, "ram": 63,
        "servicios": {"ssh": "activo", "mariadb": "inactivo"},
    },
    {
        "id": 105, "nombre": "dns-01", "ip": "192.0.2.30", "rol": "dns",
        "estado": "encendido", "cpu": 18, "ram": 27,
        "servicios": {"ssh": "activo", "bind9": "activo"},
    },
    {
        "id": 106, "nombre": "backup-01", "ip": "192.0.2.40", "rol": "copias",
        "estado": "encendido", "cpu": 88, "ram": 92,
        "servicios": {"ssh": "activo", "rsync": "inactivo"},
    },
    {
        "id": 107, "nombre": "proxy-01", "ip": "192.0.2.50", "rol": "proxy",
        "estado": "apagado", "cpu": 39, "ram": 44,
        "servicios": {"ssh": "activo", "squid": "activo"},
    },
    {
        "id": 108, "nombre": "monitor-01", "ip": "192.0.2.60", "rol": "monitorizacion",
        "estado": "encendido", "cpu": 67, "ram": 72,
        "servicios": {"ssh": "inactivo", "prometheus": "activo"},
    },
]

LISTAUNO = [
    {
        "id": 101, "nombre": "web-01", "ip": "192.0.2.10", "rol": "web",
        "estado": "encendido", "cpu": 42, "ram": 55,
        "servicios": {"ssh": "activo", "nginx": "activo"},
    }
]

LISTAVACIA = []
