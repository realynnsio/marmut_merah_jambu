from django.shortcuts import render
from marmut_merah_jambu.db import fetch
from django.db import connection
import datetime
import uuid

def context_user_getter(request):
    user = {
        'nama': request.session.get('nama'),
        'email': request.session.get('email'),
        'roles': request.session.get('roles'),
        'premium_status': request.session.get('premium_status')
    }
    return user

def get_paket():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM marmut.PAKET")
        result = fetch(cursor)
    return result

def show_list_paket(request):
    paket = get_paket()
    context = {'paket': paket}
    return render(request, "langganan.html", context)


def show_pembayaran(request):
    jenis = request.GET.get('jenis')
    harga = request.GET.get('harga')

    context = {
        'jenis': jenis,
        'harga': harga,
    }
    return render(request, "pembayaran.html", context)

def submit_payment(request):
    if request.method == "POST":
        user = context_user_getter(request)
        jenis_paket = request.POST.get('jenis')
        nominal =  request.POST.get('harga')
        metode_bayar = request.POST.get('metode_bayar')
        

        if (jenis_paket == "1 Bulan"):
            month_duration = 1
        elif (jenis_paket == "3 Bulan"):
            month_duration = 3
        elif (jenis_paket == "6 Bulan"):
            month_duration = 6
        elif (jenis_paket == "1 Tahun"):
            month_duration = 12

        # date_value = request.session["date_value"]
        # timestamp_dimulai = datetime.datetime.strptime(date_value,"%Y-%m-%d %H:%M:%S" )
        timestamp_dimulai = '2023-09-02 13:57:24'
        timestamp_dimulai_datetime = datetime.datetime.strptime(timestamp_dimulai, "%Y-%m-%d %H:%M:%S")
        timestamp_berakhir = timestamp_dimulai_datetime +datetime.timedelta(month_duration)
        timestamp_berakhir_string = timestamp_berakhir.strftime('%Y-%m-%d %H:%M:%S')
        # todo:
        # get email
        # set email
        email = 'usermarmut5@gmail.com'
        id = uuid.uuid4()
        with connection.cursor() as cursor:
            cursor.execute(""" INSERT INTO marmut.TRANSACTION (id, jenis_paket, email, timestamp_dimulai, timestamp_berakhir, metode_bayar, nominal) 
            VALUES (%s,%s,%s,%s,%s,%s,%s)""", (str(id), jenis_paket, email, timestamp_dimulai, timestamp_berakhir_string, metode_bayar, nominal))
        cursor.close()
        with connection.cursor() as cursor:
            cursor.execute("""SELECT T.jenis_paket AS jenis, T.timestamp_dimulai as mulai, T.timestamp_berakhir as berakhir, T.metode_bayar as metode, T.nominal as nominal FROM marmut.TRANSACTION T 
                        WHERE T.email = %s""", [email])
            result = fetch(cursor)
        context = {'hasil' : result}
    return render(request, "Riwayat.html", context)

def show_riwayat(request):
    user = context_user_getter(request)
    with connection.cursor() as cursor:
        email = user.get('email')
        cursor.execute("""SELECT T.jenis_paket AS jenis, T.timestamp_dimulai as mulai, T.timestamp_berakhir as berakhir, T.metode_bayar as metode, T.nominal as nominal FROM marmut.TRANSACTION T 
                       WHERE T.email = %s""", [email])
        result = fetch(cursor)
    context = {'hasil' : result}
    return render(request, "Riwayat.html", context)




# def test():
#     with connection.cursor() as cursor: 
#         cursor.execute("""SELECT * FROM marmut.PAKET;""")
#         list=fetch(cursor)
#     print(list)


# test()