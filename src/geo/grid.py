from src.geo.point import Point
import math

def spiral_itr(center=Point(0,0), initial_dir=Point(1,0), turn_cw=True):
    turn_vec = Point(1, -1) if turn_cw else Point(-1, 1)
    sign_check = Point(
            initial_dir.x + initial_dir.y * turn_vec.y,
            initial_dir.y + initial_dir.x * turn_vec.x
    )
    current_dir = initial_dir
    current_pos = center
    _turn = lambda p : Point(p.y * turn_vec.x, p.x * turn_vec.y)
    def _should_turn(current_pos, current_dir):
        confirm_pos = current_pos - center
        if current_dir == initial_dir:
            confirm_pos -= initial_dir
            confirm_sign = Point(
                    math.copysign(1, confirm_pos.x),
                    math.copysign(1, confirm_pos.y)
            )
            if confirm_pos != Point(0, 0) and confirm_sign != sign_check:
                return False
        return math.fabs(confirm_pos.x) == math.fabs(confirm_pos.y)

    while True:
        yield current_pos

        current_pos += current_dir
        if _should_turn(current_pos, current_dir):
            current_dir = _turn(current_dir)
