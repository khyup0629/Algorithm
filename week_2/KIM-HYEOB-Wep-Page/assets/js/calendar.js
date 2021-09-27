// https://bigtop.tistory.com/64?category=827794 사이트 참조
let date = new Date();

const renderCalendar = () => {
    const viewYear = date.getFullYear();
    const viewMonth = date.getMonth();

    if (viewMonth < 9) {
        document.querySelector('.year-month').textContent = `${viewYear}. 0${viewMonth + 1}.`;
    }
    else {
        document.querySelector('.year-month').textContent = `${viewYear}. ${viewMonth + 1}.`;
    }

    const prevLast = new Date(viewYear, viewMonth, 0);  // 저번 달의 마지막 날
    const thisLast = new Date(viewYear, viewMonth+1, 0);  // 이번 달의 마지막 날

    const PLDate = prevLast.getDate();  // 저번 달 마지막 날의 '일'
    const PLDay = prevLast.getDay();  // 저번 달 마지막 날의 '요일'

    const TLDate = thisLast.getDate();  // 이번 달 마지막 날의 '일'
    const TLDay = thisLast.getDay();  // 이번 달 마지막 날의 '요일'

    const scheduleMonth = [7, 9, 9, 10];  // 스케줄이 있는 월
    const scheduleDate = [7, 11, 25, 7];  // 스케줄이 있는 일(월 인덱스와 대응되도록)

    // 지난 달 날짜와 다음 달 날짜는 상황에 따라 그릴 수도, 그리지 않을 수도 있기 때문에 일단 초기값은 빈 배열
    const prevDates = [];
    const thisDates = [...Array(TLDate + 1).keys()].slice(1); // 0~TLDate의 배열이 생성되는 것에서 앞에 0을 자릅니다.
    const nextDates = [];

    if (PLDay !== 6) {  // 요일이 6, 즉 토요일이면, 앞을 그릴 필요가 없습니다.
        for (let i = 0; i < PLDay + 1; i++) {
            prevDates.unshift(PLDate - i);
        }
    }

    for (let i = 1; i < 7 - TLDay; i++) {
        nextDates.push(i);
    }

    const dates = prevDates.concat(thisDates, nextDates);  // 세 배열을 합칩니다.
    const firstDateIndex = dates.indexOf(1);  // dates 배열 요소 중 '1'이 가장 처음으로 나오는 인덱스 반환
    const lastDateIndex = dates.lastIndexOf(TLDate);  // dates 배열 요소 중 '마지막 일'이 가장 마지막으로 나오는 인덱스 반환
    dates.forEach((date, i) => {  // dates의 전체 배열을 순서대로 탐색합니다.
        condition = i >= firstDateIndex && i <= lastDateIndex
        ? 'this'
        : 'other';  // 1~마지막 일 사이에 있지 않은 수들은 class="other"로 분류해 투명 처리
        // 이번 달 date와 다른 달 date 구분
        thisMonth = i >= firstDateIndex && i <= lastDateIndex
        ? 'thisMonth'
        : 'otherMonth';
        // 스케줄이 있는 날 체크
        let scheduleOn = 'scheduleOff'
        let scheduleMark = '';
        for (let i = 0; i < scheduleMonth.length; i++) {
            if (scheduleMonth[i] === viewMonth + 1 && scheduleDate[i] === date) {
                scheduleOn = 'scheduleOn'
                scheduleMark = '🕒';
            }
        }
        dates[i] = `<div class="date ${thisMonth} ${scheduleOn}">${scheduleMark}<span class="${condition}">${date}</span></div>`;
    })

    document.querySelector('.dates').innerHTML = dates.join('');

    const today = new Date();

    if (viewMonth === today.getMonth() && viewYear === today.getFullYear()) {
        for (let date of document.querySelectorAll('.this')) {
            if (+date.innerText === today.getDate()) {
                date.classList.add('today');
                break;
            }
        }
    }
}

renderCalendar();

const prevMonth = () => {
    date.setMonth(date.getMonth() - 1);
    renderCalendar();
}

const nextMonth = () => {
    date.setMonth(date.getMonth() + 1);
    renderCalendar();
}

const goToday = () => {
    date = new Date();
    renderCalendar();
}

