//格式化时间
export function formatDate(dat) {
    //获取年月日，时间
    var year = dat.getFullYear();
    var mon = (dat.getMonth() + 1) < 10 ? "0" + (dat.getMonth() + 1) : dat.getMonth() + 1;
    var data = dat.getDate() < 10 ? "0" + (dat.getDate()) : dat.getDate();
    var hour = dat.getHours() < 10 ? "0" + (dat.getHours()) : dat.getHours();
    var min = dat.getMinutes() < 10 ? "0" + (dat.getMinutes()) : dat.getMinutes();
    var seon = dat.getSeconds() < 10 ? "0" + (dat.getSeconds()) : dat.getSeconds();

    var newDate = year + "-" + mon + "-" + data + " " + hour + ":" + min + ":" + seon;
    return newDate;
}