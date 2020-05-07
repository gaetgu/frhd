let gotoOne = () => $.scrollTo($("#one"), 800);
let gotoTop = () => $.scrollTo($("#top"), 800);
 
$("#topArrow").click(gotoOne);
$("#bottomArrow").click(gotoTop);
