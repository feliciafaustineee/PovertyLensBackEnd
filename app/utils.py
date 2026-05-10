import pandas as pd

df = pd.read_csv("data/data_with_cluster.csv")

df["Provinsi"] = df["Provinsi"].str.lower().str.strip()
df["Kab/Kota"] = df["Kab/Kota"].str.lower().str.strip()

# tingkat kemiskinannya 
def map_cluster(x):
    mapping = {
        0: {"label": "sedang", "color": "yellow"},
        1: {"label": "rendah", "color": "green"},
        2: {"label": "tinggi", "color": "red"}
    }
    return mapping[x]

# udah sesuai cluster di colab
def get_all_data():

    result = []
    
    for _, row in df.iterrows():
        cluster_info = map_cluster(row["Cluster"])
        
        result.append({
            "provinsi": row["Provinsi"],
            "kab_kota": row["Kab/Kota"],
            "cluster_id": int(row["Cluster"]),
            "cluster_label": cluster_info["label"],
            "color": cluster_info["color"]
        })
    
    return result

def get_region(name):
    name = name.lower().strip()
    
    data = df[df["Kab/Kota"].str.contains(name)]
    
    if data.empty:
        return {"error": "Region not found"}
    
    row = data.iloc[0]

    cluster_info = map_cluster(row["Cluster"])
    
    return {
    "provinsi": row["Provinsi"],
    "kab_kota": row["Kab/Kota"],
    "cluster_id": int(row["Cluster"]),
    "cluster_label": cluster_info["label"],
    "color": cluster_info["color"],

    "pendidikan": float(row["Rata-rata Lama Sekolah Penduduk 15+ (Tahun)"]),
    "pengeluaran": int(row["Pengeluaran per Kapita Disesuaikan (Ribu Rupiah/Orang/Tahun)"]),

    "tenaga_kerja": {
        "pengangguran": float(row["Tingkat Pengangguran Terbuka"]),
        "tpak": float(row["Tingkat Partisipasi Angkatan Kerja"])
    },

    "kualitas_hidup": {
        "sanitasi": float(row["Persentase rumah tangga yang memiliki akses terhadap sanitasi layak"]),
        "air_minum": float(row["Persentase rumah tangga yang memiliki akses terhadap air minum layak"])
    },

    "kemiskinan": round(float(row["Persentase Penduduk Miskin (P0) Menurut Kabupaten/Kota (Persen)"]), 2),

    # Nilai scaled (z-score) — ditampilkan sebagai skor relatif
    "ipm":               round(float(row["Indeks Pembangunan Manusia"]), 2),
    "umur_harapan_hidup": round(float(row["Umur Harapan Hidup (Tahun)"]), 2),
    "pengangguran":       round(float(row["Tingkat Pengangguran Terbuka"]), 2),
    "pdrb":               round(float(row["PDRB atas Dasar Harga Konstan menurut Pengeluaran (Rupiah)"]), 2),
    
}

def search_region(query):
    query = query.lower()
    data = df[df["Kab/Kota"].str.contains(query, na=False)]
    return data["Kab/Kota"].tolist()