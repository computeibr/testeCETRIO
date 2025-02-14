from django.db import models
import os

class DocumentType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 
    class Meta:
        ordering = ['name']
        verbose_name = 'Tipo de Documento'
    
    def __str__(self):
        return self.name
    
class Origin(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 
    class Meta:
        ordering = ['name']
        verbose_name = 'Origem'
    
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 
    class Meta:
        ordering = ['name']
        verbose_name = 'Status'
    
    def __str__(self):
        return self.name

class ClosureType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 
    class Meta:
        ordering = ['name']
        verbose_name = 'Tipo Fechamento'
    
    def __str__(self):
        return self.name

class Neighborhood(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 
    class Meta:
        ordering = ['name']
        verbose_name = 'Bairro'
    
    def __str__(self):
        return self.name

class Ap(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 
    class Meta:
        ordering = ['name']
        verbose_name = 'AP'
    
    def __str__(self):
        return self.name
    
class Closing(models.Model):
    year = models.IntegerField(verbose_name="ANO")
    monitoring_date = models.DateField(verbose_name="MONITOR")
    documenttype = models.ForeignKey(DocumentType, on_delete=models.PROTECT, related_name='closures', verbose_name='Tipo Documento')
    process_number = models.CharField(max_length=100, verbose_name="NUMERO")
    document_date = models.DateField(verbose_name="DATA DO DOC.", blank=True, null=True)
    ordinance_number = models.CharField(max_length=100, verbose_name="Nº DA PORTARIA", blank=True, null=True)
    ordinance_date = models.DateField(verbose_name="DATA DA PORTARIA OU AUTORIZACAO", blank=True, null=True)
    origin = models.ForeignKey(Origin, on_delete=models.PROTECT, related_name='closures', verbose_name='Origem')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='closures', verbose_name='Status')
    history = models.TextField(verbose_name="HISTORICO", blank=True, null=True)
    street = models.CharField(max_length=255, verbose_name="LOGRADOURO")
    reference = models.CharField(max_length=255, verbose_name="REFERENCIA", blank=True, null=True)
    closuretype = models.ForeignKey(ClosureType, on_delete=models.PROTECT, related_name='closures', verbose_name='Tipo Fechamento')
    address = models.CharField(max_length=255, verbose_name="ENDEREÇO")
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.PROTECT, related_name='closures', verbose_name='Bairro')
    ap = models.ForeignKey(Ap, on_delete=models.PROTECT, related_name='closures', verbose_name='AP')
    exit_1 = models.DateField(verbose_name="SAIDA 1", blank=True, null=True)
    destination_1 = models.ForeignKey(Origin, on_delete=models.PROTECT, related_name='destination_1_closures', verbose_name='Destino 1', blank=True, null=True)
    return_1 = models.DateField(verbose_name="RETORNO 1", blank=True, null=True)
    exit_2 = models.DateField(verbose_name="SAIDA 2", blank=True, null=True)
    destination_2 = models.ForeignKey(Origin, on_delete=models.PROTECT, related_name='destination_2_closures', verbose_name='Destino 2', blank=True, null=True)
    return_2 = models.DateField(verbose_name="RETORNO 2", blank=True, null=True)
    exit_3 = models.DateField(verbose_name="SAIDA 3", blank=True, null=True)
    destination_3 = models.ForeignKey(Origin, on_delete=models.PROTECT, related_name='destination_3_closures', verbose_name='Destino 3', blank=True, null=True)
    return_3 = models.DateField(verbose_name="RETORNO 3", blank=True, null=True)
    exit_4 = models.DateField(verbose_name="SAIDA 4", blank=True, null=True)
    destination_4 = models.ForeignKey(Origin, on_delete=models.PROTECT, related_name='destination_4_closures', verbose_name='Destino 4', blank=True, null=True)
    return_4 = models.DateField(verbose_name="RETORNO 4", blank=True, null=True)
    exit_5 = models.DateField(verbose_name="SAIDA 5", blank=True, null=True)
    destination_5 = models.ForeignKey(Origin, on_delete=models.PROTECT, related_name='destination_5_closures', verbose_name='Destino 5', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    croqui = models.TextField(verbose_name="JSON", blank=True, null=True)
    portaria = models.FileField(upload_to='concierge/', blank=True, null=True)
    observation = models.TextField(verbose_name="Observações", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 
     # Sobrescrever o Método save no Modelo
    def save(self, *args, **kwargs):
        # Verificar se o objeto já existe no banco de dados
        if self.pk:
            # Buscar o objeto atual no banco
            old_portaria = Closing.objects.get(pk=self.pk).portaria
            # Comparar se a imagem foi alterada
            if old_portaria and old_portaria != self.portaria:
                # Remover a imagem antiga do sistema de arquivos
                if os.path.isfile(old_portaria.path):
                 os.remove(old_portaria.path)
        # Salvar o novo registro
        super().save(*args, **kwargs) 

     # Sobrescrever o Método delete para Remover a Imagem
    def delete(self, *args, **kwargs):
        # Remover a imagem associada ao objeto
        if self.portaria and os.path.isfile(self.portaria.path):
            os.remove(self.portaria.path)
        # Excluir o registro
        super().delete(*args, **kwargs)



    
    class Meta:
        ordering = ['id']
        verbose_name = 'Fechamento'
    
    def __str__(self):
        return f"{self.process_number} - {self.street}"
 
 

    
""" class Origin(models.Model):
    name = models.CharField(max_length=255, verbose_name='Origem')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 
    class Meta:
        ordering = ['name']
        verbose_name = 'Origem'
    
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=255, verbose_name='Status')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 
    class Meta:
        ordering = ['name']
        verbose_name = 'Status'
    
    def __str__(self):
        return self.name
    

class Requesttype(models.Model):
    name = models.CharField(max_length=255, verbose_name='Tipo de Requisição')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 
    class Meta:
        ordering = ['name']
        verbose_name = 'Tipo de Solicitação'
    
    def __str__(self):
        return self.name
    
class Ap(models.Model):
    name = models.CharField(max_length=255, verbose_name='Área de Planejamento')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 
    class Meta:
        ordering = ['name']
        verbose_name = 'AP'
    
    def __str__(self):
        return self.name

class Neighborhood(models.Model):
    name = models.CharField(max_length=255, verbose_name='Bairro')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 
    class Meta:
        ordering = ['name']
        verbose_name = 'Bairro'
    
    def __str__(self):
        return self.name """