from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_PacketIn(event):

    packet = event.parsed

    if not packet.parsed:
        return

    src = packet.src
    dst = packet.dst

    log.info("Packet Captured")
    log.info("Source MAC: %s", src)
    log.info("Destination MAC: %s", dst)


def launch():

    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Packet Logger Module Loaded")
