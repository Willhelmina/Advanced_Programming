import Geometry.area.circle
import Geometry.area.rectangle
import Geometry.area.square
import Geometry.area.triangles
import Geometry.surface_area.cube
import Geometry.surface_area.cuboid
import Geometry.surface_area.cylinder
import Geometry.surface_area.sphere
import Geometry.volume.cube
import Geometry.volume.cuboid
import Geometry.volume.cylinder
import Geometry.volume.sphere


def main():
    #area test
    print(Geometry.area.circle.circle_area(3))
    print(Geometry.area.rectangle.rectangle_area(3,4))
    print(Geometry.area.square.square_area(3))
    print(Geometry.area.triangles.triangles_area(3,4))
    #suface area test
    print(Geometry.surface_area.cube.cube_surface(3))
    print(Geometry.surface_area.cuboid.cuboid_surface(3,4,5))
    print(Geometry.surface_area.cylinder.cylinder_surface(3,4))
    print(Geometry.surface_area.sphere.sphere_surface(3))
    #volume test
    print(Geometry.volume.cube.cube_volume(3))
    print(Geometry.volume.cuboid.cuboid_volume(3,4,5))
    print(Geometry.volume.cylinder.cylinder_volume(3,4))
    print(Geometry.volume.sphere.sphere_volume(3))
    
if __name__ == "__main__":
    main()

