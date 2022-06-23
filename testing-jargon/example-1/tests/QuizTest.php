<?php
namespace Tests;
use PHPUnit\Framework\TestCase;

class QuizTest extends TestCase {
	/** @test */
	public function it_consists_of_questions() {
		$quiz = new Quiz();
		$quiz->addQuestion(new Question("2 + 2", 4));
		#$this->assertCount(1, $quiz->questions);

		$question = $quiz->$nextQuestion();
		$question->answer(2);
		$this->assertEquals(100, $quiz->grade());
	}
}

?>
