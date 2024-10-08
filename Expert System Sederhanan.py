rules = {
    "P001": {"G1", "G2", "G3", "G4", "G5"},  # Bulai
    "P002": {"G6", "G7", "G8", "G9", "G10"},  # Blight
    "P003": {"G10", "G11", "G12", "G13", "G14"},  # Karat Daun
    "P004": {"G15", "G16", "G17", "G18", "G19"},  # Burn
    "P005": {"G20", "G21", "G22", "G23", "G24"},  # Stem Borer
    "P006": {"G28", "G29", "G30", "G31"}  # Cob Borer
}


symptoms = {
    "G1": "Daun berwarna klorotik",
    "G2": "Terjadi hambatan pertumbuhan",
    "G3": "Warna putih seperti tepung pada permukaan daun",
    "G4": "Daun menggulung",
    "G5": "Pembentukan tongkol terganggu",
    "G6": "Daun terlihat layu",
    "G7": "Bercak kecil menyatu menjadi lebih besar",
    "G8": "Bercak coklat terang memanjang berbentuk spiral",
    "G9": "Bercak coklat berbentuk elips",
    "G10": "Daun terlihat kering",
    "G11": "Bercak kecil coklat atau kuning",
    "G12": "Bercak merah pada tulang daun",
    "G13": "Serbuk seperti tepung kuning kecoklatan",
    "G14": "Benang putih pada daun",
    "G15": "Pembengkakan pada tongkol",
    "G16": "Jamur putih hingga hitam pada biji",
    "G17": "Biji bengkak",
    "G18": "Kelenjar terbentuk di biji",
    "G19": "Kelobot terbuka, banyak jamur hitam",
    "G20": "Terdapat lubang kecil di daun",
    "G21": "Garis celah pada batang",
    "G22": "Bunga jantan atau pangkal tongkol rusak",
    "G23": "Tangkai bunga mudah patah",
    "G24": "Tumpukan serbuk di sekitar tangkai",
    "G28": "Lubang melintang di daun saat vegetatif",
    "G29": "Rambut tongkol terpotong/berkurang/mengering",
    "G30": "Ujung tongkol berlubang",
    "G31": "Terdapat larva"
}


diseases = {
    "P001": "Bulai",
    "P002": "Blight",
    "P003": "Karat Daun",
    "P004": "Burn",
    "P005": "Stem Borer",
    "P006": "Cob Borer"
}

def forward_chaining(input_symptoms):
    detected_diseases = []
    possible_diseases = []

    for disease, disease_symptoms in rules.items():
        matched_symptoms = disease_symptoms.intersection(input_symptoms)

        if matched_symptoms == disease_symptoms:
            detected_diseases.append(diseases[disease])

        elif matched_symptoms:
            possible_diseases.append((diseases[disease], matched_symptoms))
    
    if detected_diseases:
        return detected_diseases, possible_diseases
    else:
        return [], possible_diseases

def input_gejala():
    print("Daftar gejala:")
    for code, description in symptoms.items():
        print(f"{code}: {description}")
    
    print("\nMasukkan kode gejala yang Anda lihat (pisahkan dengan koma, contoh: G1,G2,G3):")
    input_data = input("Gejala: ")
    input_list = set(input_data.split(","))
    return input_list

def display_possibilities(possibilities):
    print("\nBerdasarkan gejala yang dimasukkan, ada beberapa kemungkinan penyakit:")
    for disease, matched_symptoms in possibilities:
        print(f"- Kemungkinan penyakit: {disease}")
        print(f"  Gejala yang cocok: {', '.join([symptoms[g] for g in matched_symptoms])}")
        print(f"  Perlu verifikasi gejala lainnya untuk memastikan.")

if __name__ == "__main__": 
    input_symptoms = input_gejala()
    diagnosis, possibilities = forward_chaining(input_symptoms)
    
    if diagnosis:
        print("\nDiagnosis penyakit berdasarkan gejala yang dimasukkan:")
        for disease in diagnosis:
            print(f"- {disease}")
    else:
        print("\nTidak ada penyakit yang terdeteksi secara pasti berdasarkan gejala yang diberikan.")
    
    if possibilities:
        display_possibilities(possibilities)
