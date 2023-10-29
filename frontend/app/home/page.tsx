"use client";
import Levels from "@/components/levels";
import MicButton from "@/components/mic_button";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { ArrowRightSquare, MoveRight } from "lucide-react";
import { useState, useEffect } from "react";
import {
  useGetWordQuery,
  ResponseData,
} from "@/hooks/query/use-get-word-query";
import {
  useGetSentenceQuery,
  ResponseDataSentence,
} from "@/hooks/query/use-get-sentence";

export default function Home() {
  const [returnString, setReturnString] = useState<JSX.Element | null>(null);
  const [testWord, setTestWord] = useState("");
  const [firstWord, setFirstWord] = useState(true);
  const [displayWords, setDisplayWords] = useState(true); // Initial display state

  const wordQuery = useGetWordQuery({
    onSuccess(data: ResponseData) {
      console.log("success");
      console.log(data);
      setReturnString(null);
      setTestWord(data.word);
    },
  });

  const sentenceQuery = useGetSentenceQuery({
    onSuccess(data: ResponseDataSentence) {
      console.log("success");
      console.log(data);
      setReturnString(null);
      setTestWord(data.word);
    },
  });

  useEffect(() => {
    //CALL MUTATE FUNC (or get api endpoint) to get a word;
    if (firstWord){
      wordQuery.refetch();
      console.log("shmoovin");
      setFirstWord(false);
    }
  }, [displayWords]);

  // Function to fetch data based on 'displayWords'
  const fetchData = async () => {
    if (displayWords) {
      wordQuery.refetch();
      // Fetch word data
    } else {
      sentenceQuery.refetch()
      // Fetch sentence data
    }
  };

  useEffect(() => {
    fetchData();
  }, [displayWords]);

  return (
    <div className="flex min-h-screen flex-col items-center justify-center p-24">
      <Card className="min-w-[40vw] min-h-[20vh] flex justify-center align-middle items-center m-2">
        <CardContent className="font-black text-7xl text-center">
          {returnString !== null ? returnString : testWord}
        </CardContent>
      </Card>
      <div
        className={`flex flex-row flex-wrap content-center w-[40vw] ${
          returnString !== null ? "justify-between" : "justify-center"
        }`}
      >
        <MicButton returningString={setReturnString} word={testWord} />
        <Button
          variant={"link"}
          className="m-2 hover:text-purple-800"
          onClick={async () => {
            setDisplayWords(!displayWords); // Toggle between words and sentences
          }}
        >Toggle Display Between Sentences and Words
        </Button>
        {returnString!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !==
        null ? (
          <div>
            <Button
              variant={"link"}
              className="m-2 hover:text-purple-800"
              onClick={async () => {
                fetchData(); // Refetch data based on display state
              }}
            >
              <MoveRight size={48} />
            </Button>
          </div>
        ) : null}
      </div>
    </div>
  );
}
