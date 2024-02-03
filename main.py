import vtk

def main():
    # STL-Datei laden
    reader = vtk.vtkSTLReader()
    reader.SetFileName("3DBenchy.stl")

    # Mapper erstellen
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    # Actor erstellen
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    r = 32 / 255.0
    g = 157 / 255.0
    b = 80 / 255.0

    actor.GetProperty().SetColor(r, g, b)  # Skaliertes Grün

    # Renderer erstellen
    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(1.0, 1.0, 1.0)  # Hintergrundfarbe

    # RenderWindow erstellen
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)


    # RenderWindowInteractor erstellen
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Transformation erstellen
    transform = vtk.vtkTransform()
    transform.RotateZ(45)  # 45 Grad um die Z-Achse rotieren

    actor.SetUserTransform(transform)

    # Fenster initialisieren und anzeigen
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == "__main__":
    main()
