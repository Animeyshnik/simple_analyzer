settings = {}
with open('/home/animeyshnik/Documents/simple_analyzer/simple_analyzer/config/config.txt') as f:
    for line in f:
        key, value = line.strip().split("=")
        settings[key] = int(value)

print(settings["interval"])
print(settings["sequence_length"])
