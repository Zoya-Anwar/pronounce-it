import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-2xl font-bold pb-10">some random app</h1>
      <Button className="font-bold w-24">Start</Button>
    </main>
  );
}
