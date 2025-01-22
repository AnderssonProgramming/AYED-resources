def clavos(secu, pos, vel):
    if vel == 0 and secu[pos] == "T":
        return True
    elif vel == 0 and secu[pos] == "F":
        return False
    else:
        for i in range(-1, 1):
            if secu[pos + i] == "T":
                return clavos(secu, pos + i, vel + i)
            else:
                return False