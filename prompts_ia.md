# Bitácora de uso de IA — Hito 3 TI3041

**Asistente utilizado:** Claude (Anthropic), como tutor de programación.

## Prompt 1 — Depuración de la conexión MySQL (RTCF)
- **Rol:** Actúa como un tutor experto en Django y MySQL.
- **Tarea:** Explica por qué obtengo el error 1049 (Unknown database) y cómo corregirlo.
- **Contexto:** Proyecto Django con MySQL local verificado en Workbench. En settings.py el NAME era 'bluesstore', pero el esquema creado se llama instrumentos_db.
- **Formato:** Primero la causa en 2 líneas, luego los pasos de corrección y cómo comprobarlo.
- **Resultado:** Corregí NAME a 'instrumentos_db'. Aprendí que NAME debe coincidir con el esquema existente.

## Prompt 2 — Seguridad en CBVs (RTCF)
- **Rol:** Actúa como un tutor de Django que explica para defender el trabajo ante un docente.
- **Tarea:** Protege las vistas Create, Update y Delete con LoginRequiredMixin y agrega mensajes de éxito.
- **Contexto:** App "instrumentos", modelo Instrumento con FK a Categoria, Django 6.1 y Bootstrap 5. El catálogo debe seguir público.
- **Formato:** Código completo de views.py, indicando el archivo, y una explicación breve del orden de herencia (MRO).
- **Resultado:** Apliqué LoginRequiredMixin a la izquierda de SuccessMessageMixin y revisé en el navegador que /nuevo/ redirige a /accounts/login/?next=/nuevo/.