"use client";
import Levels from "@/components/levels";
import { Button } from "@/components/ui/button";
import { useState } from "react";

export default function Root() {
  const [show, setShow] = useState(true);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-gradient-to-t from-purple-800">
      <div className="flex h-5 items-center space-x-4">
        {show ? (
          <>
            <div className="row">
              <h1 className="text-9xl font-bold pb-10">
                apprenons le français
              </h1>
              <Button
                size="llg"
                className="font-bold m-2 min-w-[40rem] w-40 text-4xl"
                onClick={() => setShow(!show)}
              >
                {" "}
                Start{" "}
              </Button>
            </div>
          </>
        ) : null}
        {show ? null : <Levels />}
      </div>
    </main>
  );
}
