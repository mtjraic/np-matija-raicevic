def prosjecna_cijena(cijene):
    if not cijene:
        raise ValueError("Lista cijena ne smije biti prazna.")

    return sum(cijene) / len(cijene)
