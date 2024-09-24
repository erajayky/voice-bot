import { CheckIcon } from "lucide-react";
import Link from "next/link";
// @link https://github.com/vercel/next.js/issues/58615#issuecomment-1839619903
// Force-dynamic required to avoid a noindex tag
export const dynamic = "force-dynamic";
export default function PaymentSuccess() {
  return (
    <>
      {/* CTA Section: Simple With Logo */}
      <div className="">
        <div className="container mx-auto space-y-8 px-4 py-16 lg:px-8 lg:py-32 xl:max-w-7xl">
          {/* Heading */}
          <div className="text-center">
            <div className="relative mx-auto mb-10 inline-flex size-20 items-center justify-center text-pink-600 dark:text-pink-300">
              <div className="absolute inset-0 rotate-6 scale-105 rounded-xl bg-pink-200 dark:bg-pink-900" />
              <div className="absolute inset-0 -rotate-6 scale-105 rounded-xl bg-pink-100 dark:bg-pink-800" />

              <div className="relative">
                <CheckIcon className="hi-solid hi-fire inline-block h-16 w-16 text-pink-600" />
              </div>
            </div>
            <h2 className="mb-4 text-4xl font-black text-black dark:text-white">
              Payment completed successfully! 🎉{" "}
            </h2>
            <h3 className="mx-auto text-xl font-medium leading-relaxed text-gray-700 lg:w-2/3 dark:text-gray-300">
              Thank you for successfully completing the payment. Kindly register
              your GitHub account on the dashboard to gain access to the Dev
              Starter Boilerplate repository. Happy coding!{" "}
            </h3>
          </div>
          {/* END Heading */}

          {/* Action */}
          <div className="text-center">
            <Link
              href="/dashboard"
              className="inline-flex items-center justify-center space-x-2 rounded-lg border border-pink-700 bg-pink-700 px-6 py-3 font-semibold leading-6 text-white hover:border-pink-600 hover:bg-pink-600 hover:text-white focus:ring focus:ring-pink-400 focus:ring-opacity-50 active:border-pink-700 active:bg-pink-700 dark:focus:ring-pink-400 dark:focus:ring-opacity-90"
            >
              <span>Go to dashboard</span>
            </Link>
          </div>
          {/* END Action */}
        </div>
      </div>
      {/* END CTA Section: Simple With Logo */}
    </>
  );
}
