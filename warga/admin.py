# warga/admin.py

from django.contrib import admin
from .models import Warga, Pengaduan


@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
    """
    Konfigurasi tampilan admin untuk model Warga.
    Field yang tersedia di model Warga:
    - nik, nama_lengkap, alamat, no_telepon, tanggal_registrasi
    """
    list_display = ['nik', 'nama_lengkap', 'no_telepon', 'tanggal_registrasi']
    search_fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
    date_hierarchy = 'tanggal_registrasi'
    ordering = ['-tanggal_registrasi']
    readonly_fields = ['tanggal_registrasi']
    
    fieldsets = (
        ('Identitas', {
            'fields': ('nik', 'nama_lengkap')
        }),
        ('Kontak & Alamat', {
            'fields': ('alamat', 'no_telepon')
        }),
        ('Informasi Sistem', {
            'fields': ('tanggal_registrasi',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Pengaduan)
class PengaduanAdmin(admin.ModelAdmin):
    """
    Konfigurasi tampilan admin untuk model Pengaduan.
    Field yang tersedia di model Pengaduan:
    - judul, deskripsi, status, tanggal_lapor, pelapor
    """
    list_display = ['judul', 'pelapor', 'status', 'tanggal_lapor']
    list_filter = ['status', 'tanggal_lapor']
    search_fields = ['judul', 'deskripsi', 'pelapor__nama_lengkap', 'pelapor__nik']
    date_hierarchy = 'tanggal_lapor'
    ordering = ['-tanggal_lapor']
    readonly_fields = ['tanggal_lapor']
    
    fieldsets = (
        ('Data Pengaduan', {
            'fields': ('pelapor', 'judul', 'deskripsi')
        }),
        ('Status & Waktu', {
            'fields': ('status', 'tanggal_lapor')
        }),
    )
    
    # Untuk mempermudah filter berdasarkan status
    list_editable = []  # Bisa ditambahkan ['status'] jika ingin edit langsung dari list