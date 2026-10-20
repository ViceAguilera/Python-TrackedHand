# Seguimiento de manos con la cámara web en Python

Seguimiento de una mano en tiempo real con la cámara web, mostrando el estado de cada dedo en consola.

![Python](https://img.shields.io/badge/Python-3-3776AB?style=flat&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)
![Estado](https://img.shields.io/badge/estado-terminado-blue?style=flat)
![Licencia](https://img.shields.io/badge/licencia-MIT-blue?style=flat)
![Último commit](https://img.shields.io/github/last-commit/ViceAguilera/Python-TrackedHand?style=flat)

<!-- Demo: agrega una captura o GIF en docs/demo.gif y descomenta la línea siguiente -->
<!-- <p align="center"><img src="docs/demo.gif" alt="Demostración del seguimiento de manos" width="800"></p> -->

## Tabla de contenidos

- [Descripción](#descripción)
- [Estado del proyecto](#estado-del-proyecto)
- [Características](#características)
- [Tecnologías](#tecnologías)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Licencia](#licencia)
- [Autor](#autor)

## Descripción

Ejercicio de visión por computador que usa el módulo `HandDetector` de `cvzone` (basado en MediaPipe) para detectar una mano, dibujar sus puntos de referencia sobre el video y calcular qué dedos están levantados.

## Estado del proyecto

**Terminado.** Ejercicio personal de visión por computador, funcional y sin cambios previstos.

## Características

- Captura a 1280x720 y vista previa reducida al 50 %.
- Detección de manos con confianza mínima 0.8.
- Impresión en consola del arreglo de dedos levantados (por ejemplo `[1, 1, 0, 0, 0]`).
- Se cierra con la tecla `q`.

## Tecnologías

- Python 3
- OpenCV
- cvzone y MediaPipe

## Requisitos

- Python 3 y una cámara web.

## Instalación

```bash
pip install opencv-python cvzone mediapipe
```

## Uso

```bash
python main.py
```

## Estructura del proyecto

```
main.py   # Captura de video, detección de mano y conteo de dedos
```

## Licencia

Distribuido bajo la licencia MIT. Ver [LICENSE](LICENSE).

## Autor

**Vicente Aguilera Arias** — [Portafolio](https://portfolio.iamsirius.cl) · [GitHub](https://github.com/ViceAguilera) · [LinkedIn](https://www.linkedin.com/in/vicenteaguilera/)
