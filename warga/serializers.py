# warga/serializers.py
from rest_framework import serializers
from .models import Warga, Pengaduan


class WargaSerializer(serializers.ModelSerializer):
    """
    Serializer untuk model Warga.
    Mengkonversi objek Warga menjadi JSON dan sebaliknya.
    """
    class Meta:
        model = Warga
        fields = '__all__'  # Atau bisa tetap spesifik: ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon']


class PengaduanSerializer(serializers.ModelSerializer):
    """
    Serializer untuk model Pengaduan.
    Menampilkan nama warga untuk memudahkan pembacaan.
    """
    # Field tambahan untuk menampilkan nama warga (read-only)
    pelapor_nama = serializers.CharField(source='pelapor.nama_lengkap', read_only=True)
    
    class Meta:
        model = Pengaduan
        fields = '__all__'
        # Jika ingin menambahkan field warga_nama:
        # fields = ['id', 'warga', 'warga_nama', 'judul', 'isi_pengaduan', 
        #           'tanggal_pengaduan', 'status', 'tanggal_selesai']

    read_only_fields = ['tanggal_lapor']