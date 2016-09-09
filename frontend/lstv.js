$(document).ready(function() {
    var d = new Date();

    var thismonth = d.getMonth() + 1;
    var today = d.getDate();

    var thisyear = d.getFullYear();
    $("#ngaysinh").val(today);
    $("#thangsinh").val(thismonth);
    $("#namsinh").val(thisyear);


    function dichCung(cungBanDau, soCungDich) {
        cungSauKhiDich = Math.floor(cungBanDau);
        cungSauKhiDich += Math.floor(soCungDich);
        if (cungSauKhiDich % 12 == 0) {
            return 12
        } else {
            return cungSauKhiDich % 12
        }
    }


    diaban = $("[cung-id]").click(function() {
        $("[cung-id]").removeClass("xungChieu");
        cungid = $(this).attr('cung-id');
        cungXungChieu = dichCung(cungid, 6);
        cungTamHop1 = dichCung(cungid, 4);
        cungTamHop2 = dichCung(cungid, 8);
        $(this).addClass("xungChieu");
        $("[cung-id=" + cungXungChieu + "]").addClass("xungChieu");
        $("[cung-id=" + cungTamHop1 + "]").addClass("xungChieu");
        $("[cung-id=" + cungTamHop2 + "]").addClass("xungChieu");
    });

    function lapLaSo(laso) {
        try {
            $.templates({
                cungDiaBan: "#cungDiaBan",
                vungThienBan: "#vungThienBan",
            });

            var tb = laso['thienBan'];
            var data = laso['thapNhiCung'];
            var thienBan = $.templates.vungThienBan.render(tb);
            $("#thienBan").html(thienBan);

            var cungTy1 = $.templates.cungDiaBan.render(data[1]);
            $("#cungTy1").html(cungTy1);

            var cungSuu = $.templates.cungDiaBan.render(data[2]);
            $("#cungSuu").html(cungSuu);

            var cungDan = $.templates.cungDiaBan.render(data[3]);
            $("#cungDan").html(cungDan);

            var cungMao = $.templates.cungDiaBan.render(data[4]);
            $("#cungMao").html(cungMao);

            var cungThin = $.templates.cungDiaBan.render(data[5]);
            $("#cungThin").html(cungThin);

            var cungTy5 = $.templates.cungDiaBan.render(data[6]);
            $("#cungTy5").html(cungTy5);

            var cungNgo = $.templates.cungDiaBan.render(data[7]);
            $("#cungNgo").html(cungNgo);

            var cungMui = $.templates.cungDiaBan.render(data[8]);
            $("#cungMui").html(cungMui);

            var cungThan = $.templates.cungDiaBan.render(data[9]);
            $("#cungThan").html(cungThan);

            var cungDau = $.templates.cungDiaBan.render(data[10]);
            $("#cungDau").html(cungDau);

            var cungTuat = $.templates.cungDiaBan.render(data[11]);
            $("#cungTuat").html(cungTuat);

            var cungHoi = $.templates.cungDiaBan.render(data[12]);
            $("#cungHoi").html(cungHoi);
            var zt = new $.Zebra_Tooltips($('.tooltips'), {
                'position': 'right',
                'max_width': 300
            });
            zt.show($('#tooltip'), true);
        } catch (error) {
            baoLoi(error);
        }

    }

    $("input#laplaso").click(function() {
        $("#laso").removeClass("anlaso");
        $.ajax({
            url: 'laso.json',
            type: 'GET',
            dataType: 'json',
            data: $('form#lstv').serialize(),
            success: function(thienBandiaBan) { lapLaSo(thienBandiaBan); },
            error: function(thienBandiaBan) { baoLoi(thienBandiaBan); }
        });
    });

    function baoLoi(data) {
        $("#laso").addClass("anlaso");
        alert("Có lỗi, không thể lấy được lá số.");
    }
});