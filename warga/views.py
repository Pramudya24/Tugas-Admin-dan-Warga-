# warga/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm

# ========== IMPOR UNTUK DRF ==========
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from .serializers import WargaSerializer, PengaduanSerializer


# ========== VIEWS UNTUK WEB (HTML) - TETAP TIDAK BERUBAH ==========
class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html' 


class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'
    

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'Warga/pengaduan_list.html'
    context_object_name = 'daftar_pengaduan'
    

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')
    

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')
    

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')


class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')
    

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')


class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')


# ========== VIEWS UNTUK API (JSON) ==========
class WargaViewSet(viewsets.ModelViewSet):
    """
    API endpoint untuk CRUD Warga.
    - GET (list & detail): Bisa diakses publik
    - POST, PUT, PATCH, DELETE: Memerlukan autentikasi
    """
    queryset = Warga.objects.all().order_by('-id')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Publik bisa lihat, perlu login untuk edit


class PengaduanViewSet(viewsets.ModelViewSet):
    """
    API endpoint untuk CRUD Pengaduan.
    - Semua operasi memerlukan autentikasi (default dari settings.py)
    - Uncomment baris di bawah untuk membatasi hanya admin
    """
    queryset = Pengaduan.objects.all().order_by('-tanggal_lapor')  # FIXED: tanggal_lapor
    serializer_class = PengaduanSerializer
    # permission_classes = [IsAuthenticated]  # Default dari settings.py
    # permission_classes = [IsAdminUser]  # Uncomment untuk hanya admin