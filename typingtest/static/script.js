window.onload = go;


function go(){

	var paras = [
				"Studying is the main source of knowledge. Books are indeed never failing friends of man. For a mature mind, reading is the greatest source of pleasure and solace to distressed minds. The study of good books ennobles us and broadens our outlook. Therefore, the habit of reading should be cultivated. A student should never confine himself to his schoolbooks only. He should not miss the pleasure locked in the classics, poetry, drama, history, philosophy etc. We can derive benefit from other’s experiences with the help of books. The various sufferings, endurance and joy described in books enable us to have a closer look at human life. They also inspire us to face the hardships of life courageously. Nowadays there are innumerable books and time is scarce. So we should read only the best and the greatest among them. With the help of books we shall be able to make our thinking mature and our life more meaningful and worthwhile.",
				"Days are not of equal value in one's life. Some bring happiness while others bring sadness. Sadness and happiness both are equally important to man's life, since they are the two sides of a coin. As we cannot forget the happiest day, we are unable to forget the saddest day of our life too. The saddest day of my life was the Diwali Day. Diwali is considered to be a happy festival and till last Diwali, it was my favorite festival. On last Diwali, my sister, my brother and I were busy lighting the fireworks. I was holding a ‘fuljhari’ in my hand and unfortunately my younger brother, who was standing just beside me, had a cracker in his hand. This cracker caught fire and a very loud explosion was heard which shook my sister and me. After that, we all could think of nothing else than blood stained cotton, bandage, dettol etc. My cousin took my brother to the doctor where he got 14 stitches in his forefinger and thumb. But at home, everybody kept cursing and blaming me for the mishap. That night, I could not sleep and I cried a lot. For next few days, I bore the burden of this blame for being responsible for this unfortunate incident. I felt deeply guilty conscious which I was able to overcome after a long time.",
				"Recently, an exhibition ‘Building A New India’ was held in the capital. It was organized by the Ministry of Information and Broadcasting, Government of India. The exhibition was set up in the Triveni Kala Sangam. The chief exhibits were photographs, novels, some sculptures by Indian modern artists presenting Indian cultural inheritance. First of all, I visited the general section of the exhibition where different charts and photographs depicting India’s development in various fields were set. Most impressive photographs among these were those showing India’s nuclear development. The second section dealt with India’s magnificent historical background. I was fascinated by the pictures of Mohanjodaro excavation. Then I saw the most beautiful and colorful section of the exhibition i.e. the cultural section. It consisted of paintings, sculptures, photographs etc. The Rajasthani and Gujarati paintings were very colourful and attractive. This exhibition, inaugurated by the Prime Minister, lasted for a week. It proved to be of great educational value. It brushed up my knowledge about India as my motherland. It enhanced my respect for my great country, India. I would very much appreciate if the Indian government organized some more such exhibitions.",
				"A teacher is called builder of the nation. The profession of teaching needs men and women with qualities of head and heart. There are many teachers in our school and a large number of teachers among them are highly qualified. I have great respect for all of them. Yet I have a special liking for Miss Y. Miss Y is a woman of great principles. She is jewel among all the teachers. Almost all the students respect her. She teaches us English. She is quite at home in this subject. She takes keen interest in teaching students. Simple living and high thinking is her motto. She is a woman of sweet temper and is always ready to help in difficulties. She treats us like her own brothers and sisters. She is an ideal teacher. It is these qualities of head and heart that have endeared Miss Y to the students and teachers alike. She is an ideal teacher in real sense of the word. She is the real model to emulate. May she live as long as there is sweet fragrance in the flowers?"];

	var curPar,corPar,wrongChar;
	var finPar;
	var isWrong,start;
	var totalChar,count_timer

	var startClock;//Its a setinterval function

	var selected_par = document.getElementById('paragh');
	var selected_time = document.getElementById('timer');
	var typing_block = document.getElementById('tBlock');
	var WPM = document.getElementById('WPM');
	var time_sec = document.getElementById('SS');
	var time_min = document.getElementById('MM');

	


	function setApp(){
		// Used to Set or Reset the Values
			count_timer = selected_time.value * 60;
			curPar = paras[selected_par.value]
			corPar = ''
			wrongChar = ''
			finPar;
			isWrong = false;
			start = true;
			totalChar = 0;
			clearInterval(startClock)
			document.getElementById('body').addEventListener('keypress',checkType);
			return 0;
	}

	paragh.onchange = function(){
		setApp()
		updatePar();
		}

	timer.onchange = function(){
		setApp();
		updatePar();	
		}



	function checkType(e){

		if(start){
			countTime(count_timer); 
			start=false
			}

		if(isWrong){
			if ( String.fromCharCode(e.keyCode) == wrongChar.charAt(0) ){
				isWrong = false;
				corPar += wrongChar.charAt(0);
				wrongChar = '';
				updatePar();

				if(e.keyCode != 13){//Not count Space 	
					totalChar++;	
					};
				} 
			}

		else{
			if( curPar.charAt(0)  == String.fromCharCode(e.keyCode) )
				{
				isWrong = false;
				totalChar++;
				corPar += curPar.charAt(0);
				} 
			else
				{
					isWrong = true;
					wrongChar = curPar.charAt(0);
				}

				curPar = curPar.slice(1);
				updatePar();					
			}
		}	

	function updatePar(){
		finPar = '<span id="correct">'+corPar+'</span><span id="wrong">'+wrongChar+'</span>'+curPar;
		typing_block.innerHTML = finPar;
		return 0;
	}



	function countTime(second){
		var sec = 0;
		var min = 0;
		startClock = setInterval(function(){	

			if( (++sec) > second ){	
				stopApp();
				return 0;
				}

			if(sec%60 == 0){	
				min += 1	
				} 
			time_sec.innerHTML = sec%60;
			time_min.innerHTML = min;
			WPM.innerHTML = 'WPM : '+ calculateWPM(sec,totalChar);
			console.log(sec,min,second)

			},999.9)
		}

			
	function calculateWPM(time,charters){
		return parseInt((charters/5)/(time/60));
		}

	function stopApp(){
		clearInterval(startClock);
		document.getElementById('body').removeEventListener('keypress',checkType);
		}


	function getRandomInt(max) {
  		return Math.floor(Math.random() * Math.floor(max));
		}
		// ***************The Main********************//
		setApp();
		updatePar();



	signUp_button = document.getElementById('signUp')
	logIn_button = document.getElementById('logIn')
	signUp_button.onclick = function(){
		signUp_form = document.getElementById('signup-form');
		signUp_form.style.height = 'auto';
		signUp_form.style.transform = 'translateX(-50%) scale(1)';
		document.getElementById('body').removeEventListener('keypress',checkType);
	}
	logIn_button.onclick = function(){
		logIn_form = document.getElementById('login-form');
		logIn_form.style.height = 'auto';
		logIn_form.style.transform = 'translateX(-50%) scale(1)';
		document.getElementById('body').removeEventListener('keypress',checkType);
	}
	
	$('#cross,#cross1').click(function(){
		$('.signup-container').css("transform","translateX(-50%) scale(0)");	
		document.getElementById('body').addEventListener('keypress',checkType);
	})

	}

