import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    """Minimal publisher node — stand-in for a RosPug status/heartbeat topic.

    Kept deliberately simple: this exists to prove the CI pipeline (build +
    test on every push), not to do real robot logic.
    """

    def __init__(self):
        super().__init__('rospug_talker') 
        self.publisher_ = self.create_publisher(String, 'rospug/status', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'RosPug heartbeat #{self.count}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
