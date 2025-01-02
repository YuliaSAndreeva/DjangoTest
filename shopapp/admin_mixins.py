import csv
from dataclasses import field

from django.db.models.options import Options

from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse


class Export_goods_mixin:
    def export_csv(self, request:HttpRequest, queryset: QuerySet):
        meta: Options = self.model._meta
        fields_name = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}-export.csv'

        csv_writer = csv.writer(response)

        csv_writer.writerow(fields_name)

        for row in queryset:
            csv_writer.writerow([getattr(row, field) for field in fields_name])

        return response

    export_csv.short_description = 'Выгрузука в CSV файл'