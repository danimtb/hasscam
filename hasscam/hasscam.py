#!/usr/bin/env python3
import pygame
import pygame.camera

pygame.camera.init()
pygame.camera.list_camera() #Camera detected or not
cam = pygame.camera.Camera("/dev/video0", (640, 480))
cam.start()
img = cam.get_image()
pygame.image.save(img, "/share/filename.jpg")



# # Catch SIGINT/SIGTERM Signals
# signal.signal(signal.SIGINT, signal_handler)
# signal.signal(signal.SIGTERM, signal_handler)

# # Remove Scapy IPv6 warnings
# logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# # Create basepath
# path = os.path.dirname(os.path.realpath(__file__))

# # Log events to stdout
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

# stdoutHandler = logging.StreamHandler(sys.stdout)
# stdoutHandler.setLevel(logging.INFO)

# formater = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
# stdoutHandler.setFormatter(formater)

# logger.addHandler(stdoutHandler)

# # Read config file
# logging.info("Reading config file: /data/options.json")


# with open(path + "/data/options.json", mode="r") as data_file:
#     config = json.load(data_file)
# data_file.close()


# while True:
#     # Start sniffing
#     logging.info("Starting sniffing...")
#     sniff(stop_filter=arp_display,
#           filter="arp or (udp and src port 68 and dst port 67 and src host 0.0.0.0)",
#           store=0, count=0, iface=conf.iface)
#     logging.info("Packet captured, waiting 20s ...")
#     time.sleep(20)
