<?php

namespace Tests\Unit;

use PHPUnit\Framework\TestCase;
use App\Quiz;
use App\Question;

class QuizTest extends TestCase
{
	/** @test */
	public function test_it_consists_of_questions() {
		$quiz = new Quiz();
		$quiz->addQuestion(new Question("2 + 2", 4));
		$this->assertCount(1, $quiz->questions());
	}

	public function test_it_can_be_grabed() {
		$quiz = new Quiz();
		$quiz->addQuestion(new Question("2 * 2", 4));
		$question = $quiz->nextQuestion();
		$question->answer(4);
		$this->assertEquals(100, $quiz->grade());
	}

}
