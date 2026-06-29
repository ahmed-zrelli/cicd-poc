import rclpy
from rospug_demo.talker import Talker


def test_talker_node_name():
    rclpy.init()
    node = Talker()
    assert node.get_name() == 'rospug_talker'
    node.destroy_node()
    rclpy.shutdown()


def test_talker_publishes_on_correct_topic():
    rclpy.init()
    node = Talker()
    topic_names = [t for t, _ in node.get_topic_names_and_types()]
    assert any('rospug/status' in t for t in topic_names)
    node.destroy_node()
    rclpy.shutdown()


def test_talker_counter_starts_at_zero():
    rclpy.init()
    node = Talker()
    assert node.count == 0
    node.timer_callback()
    assert node.count == 1
    node.destroy_node()
    rclpy.shutdown()
