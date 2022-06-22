<?php
namespace Tests;
use App\TagParser;
use PHPUnit\Framework\TestCase;

class TagParserTest extends TestCase {
	/** @dataProvider tagsGenerator */
	public function test_it_parsestags($input, $expected) {
		$parser = new TagParser();
		$result = $parser->parse($input);
		$this->assertSame($result, $expected);
	}

	public function tagsGenerator() {
		return [
			['world', ['world']],
			['love, family, money', ['love', 'family', 'money']],
			['love,family,money', ['love', 'family', 'money']],
			['love|family|money', ['love', 'family', 'money']],
			['world!war', ['world', 'war']]
		];
	}
}
?>
