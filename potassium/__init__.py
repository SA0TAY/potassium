#!/usr/bin/env python3
import configparser
import pywsjtx.extra.simple_server
from pota import POTA

MY_MAX_SCHEMA = 3
config = configparser.ConfigParser()
if not config.read("settings.ini"):
    print("Can't read settings.ini. Have you read the documentation?")
    exit(1)

pota = POTA()
s = pywsjtx.extra.simple_server.SimpleServer(config["WSJT-X"]["ip"],
    int(config["WSJT-X"]["port"]), timeout=2.0)

while True:
    (pkt, addr_port) = s.rx_packet()
    if (pkt):
        decoded_packet = pywsjtx.WSJTXPacketClassFactory.from_udp_packet(addr_port, pkt)
        if type(decoded_packet) == pywsjtx.HeartBeatPacket:
            max_schema = max(decoded_packet.max_schema, MY_MAX_SCHEMA)
            reply_beat_packet = pywsjtx.HeartBeatPacket.Builder(decoded_packet.wsjtx_id,max_schema)
            s.send_packet(addr_port, reply_beat_packet)
        if type(decoded_packet) == pywsjtx.DecodePacket:
            caller = decoded_packet.message.split()[1]
            if caller in pota.activators:
                if decoded_packet.message.split()[0] == "CQ":
                    print("{} CQ!".format(caller))
                else:
                    print("{}".format(caller))
                colour_packet = pywsjtx.HighlightCallsignPacket.Builder(decoded_packet.wsjtx_id, caller,
                    pywsjtx.QCOLOR.Red(),
                    pywsjtx.QCOLOR.White(),
                    True)
                s.send_packet(addr_port, colour_packet)
