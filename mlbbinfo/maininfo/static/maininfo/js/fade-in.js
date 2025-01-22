// Создаем observer для отслеживания видимости элементов
const observer = new IntersectionObserver(
	(entries, observer) => {
		entries.forEach((entry) => {
			if (entry.isIntersecting) {
				// Когда элемент становится видимым, добавляем класс 'visible'
				entry.target.classList.add("visible");
				// Прекращаем наблюдение за этим элементом
				observer.unobserve(entry.target);
			}
		});
	},
	{ threshold: 0.25 } // срабатывает, когда 50% элемента видны
);

// Находим все элементы, которые нужно анимировать
const fadeInElements = document.querySelectorAll(".fade-in");

// Применяем observer к каждому элементу
fadeInElements.forEach((element) => {
	observer.observe(element);
});
