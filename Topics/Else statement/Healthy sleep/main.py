def enough_sleep(hours_needed, hours_excess, hours_slept):
    if int(hours_needed) > int(hours_slept):
        print("Deficiency")
    else:
        if int(hours_excess) < int(hours_slept):
            print("Excess")
        else:
            print("Normal")

need = input()
slept = input()
excess = input()

enough_sleep(need, slept, excess)
